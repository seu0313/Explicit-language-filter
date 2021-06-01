import {
  Column,
  CreateDateColumn,
  Entity,
  PrimaryGeneratedColumn,
} from "typeorm";

@Entity()
export class Deep {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ default: null })
  title: string;

  @Column({ default: null })
  description: string;

  @Column({ default: null })
  videoFile: string;

  @Column({ default: null })
  videoDuration: number;

  @Column({ default: null })
  processMethod: string;

  @CreateDateColumn({ type: "datetime" })
  createdAt: Date;
}
